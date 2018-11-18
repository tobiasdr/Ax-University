from flask import Flask, render_template
import json

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
    return json_data;



if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
