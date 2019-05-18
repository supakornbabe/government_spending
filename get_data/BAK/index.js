"use strict";
exports.__esModule = true;
var axios_1 = require("axios");
var fs_1 = require("fs");
var link = 'https://govspendingapi.data.go.th/api/service/bbgfproject';
var params = {
    'budget_end': '1000000',
    'min_code': '02000',
    'offset': '0',
    'user_token': '402751371d8d559f36046d26b9f964d8',
    'year': '2561'
};
axios_1["default"].get(link, { params: params })
    .then(function (response) {
    var res = JSON.parse(response.data.result);
    console.log(res);
    fs_1.writeFile('test.txt', res, function (err) {
        if (err) {
            throw err;
        }
        console.log('saved!');
    });
})["catch"](function (error) { console.log(error); });
