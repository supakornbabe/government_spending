import axios from 'axios';
import {writeFile} from "fs"

const link = 'https://govspendingapi.data.go.th/api/service/bbgfproject'

const params = {
    'budget_end' : '1000000',
    'min_code' : '02000',
    'offset' : '0',
    'user_token' : '402751371d8d559f36046d26b9f964d8',
    'year' : '2561',
};
axios.get(link, {params})
    .then((response) => {
        const res = JSON.parse(response.data.result)
        console.log(res)
        writeFile('test.txt', res, (err) => {
            if (err) {
                throw err;
            }
            console.log('saved!');
        });
    })
    .catch((error) => {console.log(error)})
