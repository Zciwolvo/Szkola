const querystring = require('querystring');

exports.welcome = (req, res) => {
  const { imie, nazwisko } = req.query;
  const welcomeMessage = `Witaj ${imie} ${nazwisko}`;
  res.send(welcomeMessage);
};
