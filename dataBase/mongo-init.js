db = db.getSiblingDB('myshop');

db.products.insertMany([
    { name: 'Ice cream' },
    { name: 'Chocolate' },
    { name: 'Fruit' },
    { name: 'Potatoes' },
    { name: 'Big Mac' },
    { name: 'Eggs' }
]);
