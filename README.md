"# flask-restplus-adapis" 
___
Active Directory Rest APIs example Using
- Flaks-Restplus
- Flask-SQLAlchemy
- Blueprint

### initdb
``` python
from initdb import db, BindUserTable

db.create_all()

data = BindUserTable(username='binduser@domain.local', password='password', domain='domain.local', basedn='ou=users,dc=domain,dc=local', bindou='ou=admin,dc=domain,dc=local', serverip='192.168.1.10')

db.session.add(data)
db.session.commit()

```
#RUN @windows
``` 
set FLASK_APP=visitorapis
set FLASK_DEBUG=1
flask run --host=0.0.0.0
```

