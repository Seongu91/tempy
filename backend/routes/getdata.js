var express = require('express');
var router = express.Router();
var indexes = require('../models/indexes');

/* GET users listing. */
router.get('/', function(req, res, next) {
  indexes
    .find()
    .then(posts => {
      console.log("Read All 완료");
      res.status(200).json({
        message: "Read All success",
        data: {
          post: posts
        }
      });
    })
    .catch(err => {
      res.status(500).json({
        message: err
      });
    });
});

module.exports = router;
