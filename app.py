from flask import Flask, render_template, request
import json, requests, web3

from web3 import Web3
from eth_account.messages import defunct_hash_message
"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [{
  "Name": "Tobias Drees",
  "Date of Birth": "07.04.1997",
  "Student Number": "122347563",
  "Degree type": "MEng",
  "Status": "degree in progress",
  "Start date": "02/10/2017",
  "End date": "25/06/2021",
  "End result": "62%"
},
{
  "Name": "Peter Wallace",
  "Date of Birth": "06.12.1997",
  "Student Number": "983414545",
  "Degree type": "BSc",
  "Status": "degree in progress",
  "Start date": "02/10/2017",
  "End date": "23/06/2020",
  "End result": "71%"
}, {
  "Name": "Sirvan Almasi",
  "Date of Birth": "12.05.1995",
  "Student Number": "587362201",
  "Degree type": "BEng",
  "Status": "graduated",
  "Start date": "02/10/2013",
  "End date": "25/06/2016",
  "End result": "68%"
}
]

abi = [
    {
        "constant": True,
        "inputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "keys",
        "outputs": [
            {
                "name": "title",
                "type": "string"
            },
            {
                "name": "key",
                "type": "string"
            },
            {
                "name": "status",
                "type": "bool"
            },
            {
                "name": "comment",
                "type": "string"
            },
            {
                "name": "approver",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_url",
                "type": "string"
            }
        ],
        "name": "changeMsgServer",
        "outputs": [
            {
                "name": "outcome",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isApproved",
        "outputs": [
            {
                "name": "approved",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "omneeUser",
        "outputs": [
            {
                "name": "entityType",
                "type": "uint256"
            },
            {
                "name": "owner",
                "type": "address"
            },
            {
                "name": "msgServer",
                "type": "string"
            },
            {
                "name": "approved",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_title",
                "type": "string"
            },
            {
                "name": "_key",
                "type": "string"
            },
            {
                "name": "_comment",
                "type": "string"
            }
        ],
        "name": "addKey",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "getKey",
        "outputs": [
            {
                "name": "title",
                "type": "string"
            },
            {
                "name": "key",
                "type": "string"
            },
            {
                "name": "status",
                "type": "bool"
            },
            {
                "name": "comment",
                "type": "string"
            },
            {
                "name": "approver",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "lenKeys",
        "outputs": [
            {
                "name": "size",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "msgServer",
        "outputs": [
            {
                "name": "msgServer",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_senderAddress",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    }
]

# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "Name", # which is the field's name of data key
    "title": "Name", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Date of Birth",
    "title": "Date of Birth",
    "sortable": True,
  },
  {
    "field": "Student Number",
    "title": "Student Number",
    "sortable": True,
  },
  {
    "field": "Degree type",
    "title": "Degree type",
    "sortable": True,
  },
    {
      "field": "Status",
      "title": "Status",
      "sortable": True,
    },
    {
      "field": "Start date",
      "title": "Start date",
      "sortable": True,
    },
    {
      "field": "End date",
      "title": "End date",
      "sortable": True,
    },
    {
      "field": "End result",
      "title": "End result",
      "sortable": True,
    }

]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Student database')
# /recDID/<rDID>/myDID/<mDID>/publicKey/<publicKey>

@app.route('/changepermission/<type>')
def changePermission(type):
    data = {}
    data['Permissiontype'] = type
    json_data = json.dumps(data)
    return json_data

@app.route('/api/changepermission', methods=['Post'])
def chngPermission():
    req_data = request.get_json()

    # address of the identity holder
    #address = Web3.toChecksumAddress("0xf2beae25b23f0ccdd234410354cb42d08ed54981")

    address = Web3.toChecksumAddress(req_data['recDID'])
    # web3.py instance
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:9545"))

    # the public key we wish to verify
    # WE NEED msg AND sig
    # NOT SECURE, IN THE FUTURE RUN PROPER MSG PROCESSING
    msgHash = defunct_hash_message(text=req_data['msg'])
    verPubKey = w3.eth.account.recoverHash(msgHash, signature=req_data['sig'])
    #verPubKey = "0x627306090abab3a6e1400e9345bc60c78a8bef57"

    

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[1]
    print(Web3.toChecksumAddress(w3.eth.defaultAccount))

    # get the DID contract
    DIDContract = w3.eth.contract(
        address=address,
        abi=abi,
    )

    # search through the keys
    # get the number of keys stored on the identity contract
    lenK = DIDContract.functions.lenKeys().call()

    keyFound = False
    for i in range(0, lenK):
        key = DIDContract.functions.getKey(i).call()
        print(key[1])
        if str(key[1])==str(verPubKey):
            return "SUCCESS"
    return "FAIL"



if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
