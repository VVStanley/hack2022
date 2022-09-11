module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/static/front/' : '/',
  outputDir: '../backend/static/front/',
  indexPath: '../../templates/base-vue.html'
};
