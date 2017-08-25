var path = require('path');

/*------ Sources Variables ------*/
var uiSrcDir = path.join(__dirname, 'ui-src');
var reactAppDir = path.join(uiSrcDir, 'app');

var buildDir = path.join(__dirname, 'static');
var jsBuildDir = path.join(buildDir, 'js');
/*-------------------------------*/

module.exports = {
  entry: path.join(reactAppDir, 'index.js'),

  output: {
    path: jsBuildDir,
    filename: "app.bundle.js"
  },

  module: {
    loaders: [
      {
        test: /\.(jsx|js)$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      }
    ]
  },

  devServer: {
    inline: true,
    port: 8001,
    hot: true,
    contentBase: buildDir
  },

  watchOptions: {
    aggregateTimeout: 500,
    poll: 1000,
    ignored: /(node_modules|bower_components|static)/
  },

  node: {
    fs: 'empty'
  }
};
