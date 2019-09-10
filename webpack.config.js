const path = require('path');

module.exports = {
  mode: 'production',
  entry: './static/js/app.js',
  output: {
    path: path.resolve(__dirname, 'static/js/build')
  },
  watch: true
};
