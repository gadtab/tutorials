import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/foundation.dart';

class Kittens extends StatelessWidget {
  const Kittens({Key key}) : super(key: key);

  Widget _dialogBuilder(BuildContext context, DocumentSnapshot document) {
    ThemeData _localTheme = Theme.of(context);

    return SimpleDialog(
      contentPadding: EdgeInsets.zero,
      children: <Widget>[
        Image.network(
          document['imageUrl'],
          fit: BoxFit.fill,
        ),
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Text(document['name'], style: _localTheme.textTheme.display1,),
              Text('${document['age']} months old',
                style: _localTheme.textTheme.subhead.copyWith(
                  fontStyle: FontStyle.italic,
                ),
              ),
              SizedBox(
                height: 16.0,
              ),
              Text(document['description'], style: _localTheme.textTheme.body1,),
              SizedBox(
                height: 16.0,
              ),
              Align(
                alignment: Alignment.centerRight,
                child: Wrap(
                  children: <Widget>[
                    FlatButton(
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                      child: const Text('I\'m Alergic'),
                    ),
                    RaisedButton(
                      onPressed: () {},
                      child: const Text('Adopt'),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _listItemBuilder(BuildContext context, DocumentSnapshot document) {
    return GestureDetector(
      onTap: () =>
          showDialog(
              context: context,
              builder: (context) => _dialogBuilder(context, document)
          ),
      child: Container(
        padding: const EdgeInsets.only(left: 16.0),
        alignment: Alignment.centerLeft,
        child: Text(
          document['name'],
          style: Theme.of(context).textTheme.headline,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Available Kittens'),
      ),
      body: StreamBuilder(
          stream: Firestore.instance.collection('Kittens').snapshots(),
          builder: (context, snapshot) {
            if (!snapshot.hasData) return const Text('Loading...');

            return ListView.builder(
              itemCount: snapshot.data.documents.length,
              itemExtent: 60.0,
              itemBuilder: (context, index) =>
                  _listItemBuilder(context, snapshot.data.documents[index]),
            );
          }
      ),
    );
  }
}