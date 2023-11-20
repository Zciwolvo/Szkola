exports.nowaPage = (req, res) => {
    res.status(200).send('To jest nowa strona!');
  };
  
  exports.staraPage = (req, res) => {
    res.status(200).send('To jest stara strona!');
  };