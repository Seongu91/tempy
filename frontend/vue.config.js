module.exports = {
  configureWebpack:{
    devtool: 'source-map'
  },
  devServer: {
    disableHostCheck: true,
  },
  transpileDependencies: [
    'vuetify',
  ],
  lintOnSave : false,
}