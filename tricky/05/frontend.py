from flask import Flask
import requests
import json
import os

backend_url = 'http://0.0.0.0:8080'

# helper, who gets URL content as html
def get_request (url):

   r = requests.get(url)
   tree = html.fromstring(r.text)

   return tree

app = Flask(__name__)

@app.route("/")
def greeting():

    gcp = requests.get(backend_url + '/gcp').text
    gcp_json = json.loads(gcp)
    aws = requests.get(backend_url + '/aws_eu').text
    aws_json = json.loads(aws)
    text = gcp_json['state'] + "  " +  gcp_json['date'] + "   " + aws_json['status']
     
    return text

#@app.route("/aws_eu")
#def aws_status():
#    output = {}
#    tree = get_html(aws_url)
#    status_aws_europe_div = tree.xpath('//div[contains(@id, "EU_block")]')[0]
#    status_aws_europe_table = status_aws_europe_div.xpath('.//table')[0]
#    status_aws_europe= status_aws_europe_table.xpath('.//td[@colspan]')[0].text
#
#    if status_aws_europe :
#        output['status'] = status_aws_europe
#        output['error'] = ''
#    else:
#        output['error'] = 'Something wrong with AWS status page. Check %s', aws_url
#    return output
#
#@app.route("/status")
#def backend_status():
#    output = {}
#    output['instance_id'] = os.getenv('CF_INSTANCE_INDEX')
#    output['instance_guid'] = os.getenv('CF_INSTANCE_GUID')
#    output['instance_port'] = os.getenv('CF_INSTANCE_PORT')
#    return output
#
#@app.route("/gcp")
#def gcp_status():
#    tree = get_html(gcp_url)
#    status_gcp = tree.xpath('//span[contains(@class, "status")]')[0].text
#    status_date_gcp = tree.xpath('//span[contains(@class, "date")]')[0].text
#    output = {}
#    if status_gcp and status_date_gcp:
#        output['date'] = status_date_gcp
#        output['state'] = status_gcp
#        output['error'] = ''
#    else:
#        output['error'] = "Something wrong with GCP, check %s", gcp_url
#    return output
#
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8083 ,debug = True)
