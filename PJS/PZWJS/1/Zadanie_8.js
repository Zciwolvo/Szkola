var bufor = new Buffer.alloc(26);

for(var i=0; i<26; i++)
{
    bufor[i]=i+97;
}
console.log(bufor);
console.log('ASCII');
console.log(bufor.toString('ascii'));
console.log('UTF-8');
console.log(bufor.toString('utf8'));