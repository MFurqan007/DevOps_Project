db = db.getSiblingDB("admin");
db.auth(
  process.env.MONGO_INITDB_ROOT_USERNAME,
  process.env.MONGO_INITDB_ROOT_PASSWORD
);

db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);

db.doctors.insertMany([
  {
    id: '1',
    firstName: 'Muhammad Ali',
    lastName: 'Kahoot',
    speciality: 'DevOps'
  },
  {
    id: '2',
    firstName: 'Good',
    lastName: 'Doctor',
    speciality: 'Test'
  }
]);