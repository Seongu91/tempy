module.exports = {
  configureWebpack:{
    devtool: 'source-map'
  },
  devServer: {
    disableHostCheck: true,
    proxy: {
      '/getdata': {
        target: 'http://localhost:3000',
        changeOrigin: true
      }
    }
  },
  transpileDependencies: [
    'vuetify',
  ],
  lintOnSave : false,
}