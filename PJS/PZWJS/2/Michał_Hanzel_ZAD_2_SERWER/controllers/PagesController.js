//zmienna pomocnicza
var pages = ['home', 'second-page', 'third-page', 'fourth-page'];

//funkcje
exports.home = (req, res) => {
    res.render('home', { data: { title: pages[0], titles: pages } });
};

exports.secondPage = (req, res) => {
    res.render('home', { data: { title: pages[1], titles: pages } });
};

exports.thirdPage = (req, res) => {
    res.render('home', { data: { title: pages[2], titles: pages } });
};

exports.fourthPage = (req, res) => {
    res.render('home', { data: { title: pages[3], titles: pages } });
};