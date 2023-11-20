const http = require('http');

exports.zad3 = (url) => {
    return new Promise((resolve, reject) => {
        http.get(url, (response) => {
          let data = '';
    
          response.on('data', (chunk) => {
            data += chunk;
          });
    
          response.on('end', () => {
            resolve(data);
          });
        }).on('error', (error) => {
          reject(error);
        });
      });
}
