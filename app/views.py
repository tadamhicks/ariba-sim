from flask import Flask, request, session, redirect, url_for, \
	render_template, jsonify, make_response
from app import app, db
from .models import RequestItems
import json
import distutils

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/request', methods=['GET', 'POST'])
def requestitems():
    content_type = request.headers.get('Content-Type')
    if request.method == 'POST':

        req_data = request.get_json()

        name = req_data['name']
        morpheus_id = int(req_data['morpheus_id'])
        item = req_data['item']
        status = False
        requestor = req_data['requestor']
        price = req_data['price']

        try:
            request_item = RequestItems(name, morpheus_id, item, status, requestor, price)
            request_item.create_record()
            return jsonify(RequestItems=request_item.serialize)
        except:
            return jsonify(duplicate='true')

    else:
        if request.args.get('morpheus_id'):
            id = request.args.get('morpheus_id')
            print(id)
            #record = RequestItems(id).get_one()
            record = RequestItems.query.filter_by(morpheus_id=id).all()
            if content_type == 'application/json':
                return jsonify(data=[i.serialize for i in record])

            return render_template('request.html', record=record)
        else:
            requests = RequestItems.get_records()

        if content_type == 'application/json':
            return jsonify(data=[i.serialize for i in requests])
        return render_template('requests.html', requests=requests)

@app.route('/approval', methods=['POST'])
def approvals():
    value = request.form.get('approval').split('_')
    select = value[0]

    id = value[1]
    x = bool(distutils.util.strtobool(select))
    requestitem = RequestItems.query.filter_by(id=id).first()
    requestitem.status = x
    db.session.commit()
    return redirect(url_for('requestitems'))

'''
def makeRequestItem(name, item, status, requestor):
    requested_item = RequestItems(name=name, item=item, status=status, requestor=requestor)
    session.add(requested_item)
    session.commit()
    return jsonify(RequestItems=requested_item.serialize)
'''