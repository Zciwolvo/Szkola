// moduł odpowiedzialny za generowanie odpowiedzi
exports.home = (req, res) => {
    // wygenerowanie szablonu o nazwie home z katalogu views
     res.render('home', {
    // przesłanie dodatkowych informacji do szablonu poprzez moduł flash
     formMessage: req.flash('form')
     });
    };
    