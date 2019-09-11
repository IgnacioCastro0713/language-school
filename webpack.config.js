const path = require('path');

module.exports = {
  mode: 'production',
  entry: {
    index: './static/js/app.js',
    another: './static/js/another-app.js'
  },
  //Two packages are made that do not exceed the size recommended by Webpack.
  output: {
    filename: '[name]-bundle.js',
    path: path.resolve(__dirname, 'static/js/build')
  },
  watch: true
};
