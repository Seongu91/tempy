const mongoose = require('mongoose');

// Define Schemes
const indexesSchema = new mongoose.Schema({
  _id: { type: String },
  daily_price: { type: [] }
},
{
  collection: 'Indexes'
});

// Create Model & Export
module.exports = mongoose.model('Indexes', indexesSchema);