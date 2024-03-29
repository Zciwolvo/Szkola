const http = require('http');

exports.zad3 = () => {
    return new Promise((resolve, reject) => {
        http.get("http://igorgawlowicz.pythonanywhere.com", (response) => {
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
