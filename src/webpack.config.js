const path = require('path');

module.exports = {
  entry: './portfolio/static/portfolio/index.js',
  output: {
    path: path.resolve(__dirname, 'portfolio/static/portfolio/dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};