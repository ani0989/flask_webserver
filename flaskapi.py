from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/companies', methods=['POST'])
def post_companies():
  num = 0
  with open('workfile') as f:
    num = int(f.read())+1
  
  f = open('workfile', 'w')
  f.write("")

  new_company = {"id": num, "name": "Company {}".format(num)}
  companies.append(new_company)
  
  f = open('workfile', 'w')
  f.write(str(num))
  
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
  api.run()