// db = db.getSiblingDB('admin');

// db.auth(process.env.MONGO_ROOT_USERNAME, process.env.MONGO_ROOT_PASSWORD);

// db = db.getSiblingDB(process.env.MONGO_DATABASE);

// db.createCollection('test');

// db = db.getSiblingDB('admin');

// db.createUser({
//   user: 'admin',
//   pwd: 'password',
//   roles: [{ role: 'root', db: 'admin' }]
// });

// db.createUser({
//   user: 'pastime',
//   pwd: 'pastime123',
//   roles: [
//     {
//       role: 'readWrite',
//       db: 'pastime'    
//     }
//   ]
// })

db = db.getSiblingDB("admin");
db.auth(
  process.env.MONGO_INITDB_ROOT_USERNAME,
  process.env.MONGO_INITDB_ROOT_PASSWORD
);

db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);

db.appointments.insertMany([
  {
    id: '1',
    doctor: '1',
    date: '21 Nov 2023',
    rating: 'Good'
  },
  {
    id: '2',
    doctor: '1',
    date: '22 Nov 2023',
    rating: 'Bad'
  },
  {
    id: '3',
    doctor: '2',
    date: '22 Nov 2023',
    rating: 'Good'
  },
  {
    id: '4',
    doctor: '1',
    date: '22 Nov 2023',
    rating: 'Bad'
  },
  {
    id: '5',
    doctor: '2',
    date: '22 Nov 2023',
    rating: 'Good'
  }
]);
