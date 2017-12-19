const webpack = require('webpack');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  entry:[ 
    './feed.jsx'
  ],
  output:{
    filename:'../dist/feed.bundle.js'
  },
  module:{
    loaders:[
      {
        test:/\.js[x]?$/,
        loader:'babel-loader',
        exclude:/(node_modules)/,
        query:{
          presets:['es2015','react']
        }
      }
    ]
  },
  plugins: [
    //Minify build
    new UglifyJsPlugin(),
    //build production
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production')
    }),
    //expose jquery window global
    new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
        tether: 'tether',
        Tether: 'tether',
        'window.Tether': 'tether',
    })
  ]
};