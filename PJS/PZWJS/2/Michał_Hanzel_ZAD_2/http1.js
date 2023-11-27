var url = require('url');

var url1 = 'https://www.google.pl/search?sxsrf=ALeKk01QMi5XyKt0CNcDXskAMcgf4jaKgA%3A1611742087695&source=hp&ei=hzsRYJP2J4abrgTIyYfYBw&q=js+toutorial&oq=js+toutorial&gs_lcp=CgZwc3ktYWIQAzIHCCMQsAIQJzIGCAAQDRAeMgYIABANEB4yBggAEA0QHjIGCAAQDRAeMgYIABANEB4yBggAEA0QHjIGCAAQDRAeMgYIABANEB4yBggAEA0QHjoECCMQJzoLCAAQsQMQxwEQowI6CAgAELEDEIMBOggILhCxAxCDAToICAAQxwEQowI6AgguOgQIABBDOg4IABCxAxCDARDHARCjAjoHCAAQsQMQQzoKCC4QsQMQgwEQQzoICAAQxwEQrwE6AggAOgUIABDLAToHCAAQChDLAToICAAQFhAKEB46BggAEBYQHjoECAAQDVCEB1jgGmDCHGgAcAB4AIABWogBlAeSAQIxMpgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjT1eqU77vuAhWGjYsKHcjkAXsQ4dUDCAc&uact=5';
var url2 = 'https://www.bing.com/search?q=js+tutorial&FORM=AWRE';
var url3 = 'https://duckduckgo.com/?q=js+toutorial&t=h_&ia=web';

var type = url.parse(url1).hostname;
type = type.split(".").pop();
console.log("Type: " + type);

var query1 = url.parse(url1).query;
console.log("Query: " + query1);

var path1 = url.parse(url1).path;
console.log("Path: " + path1);

var hash1 = url.parse(url1).hash;
console.log("Hash: " + hash1);

var type2 = url.parse(url2).hostname;
type2 = type2.split(".").pop();
console.log("Type: " + type2);

var query2 = url.parse(url2).query;
console.log("Query: " + query2);

var path2 = url.parse(url2).path;
console.log("Path: " + path2);

var hash2 = url.parse(url2).hash;
console.log("Hash: " + hash2);

var type3 = url.parse(url3).hostname;
type3 = type3.split(".").pop();
console.log("Type: " + type3);

var query3 = url.parse(url3).query;
console.log("Query: " + query1);

var path3 = url.parse(url3).path;
console.log("Path: " + path3);

var hash3 = url.parse(url3).hash;
console.log("Hash: " + hash3);