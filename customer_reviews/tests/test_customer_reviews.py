from odoo.tests import common


class TestExecuteQuery(common.TransactionCase):
    def test_execute_query(self):

        customer_object = self.env["res.users"].browse(1).partner_id
        customer_id = customer_object.id
        customer_object.customer = True

        vendor_obj = self.env["res.partner"].search([("supplier", "=", True)])
        print(vendor_obj)
        vendor_id = vendor_obj[0].id
        print("vendor id : " + str(vendor_id))
        print("cusstomer id : " + str(customer_id))
        data = {}
        data["customer_id"] = customer_id
        data["vendor_id"] = vendor_id
        data["message"] = "Very Good"
        data["ratings"] = "5"

        record = self.env["customer.reviews"].create(data)
        self.assertEqual(record.vendor_id.id, vendor_id)
        self.assertEqual(record.ratings, vendor_obj[0].average_ratings)
        self.assertEqual(vendor_obj[0].number_of_rates, 1)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Test Was Successfull")
