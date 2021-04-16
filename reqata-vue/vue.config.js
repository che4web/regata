module.exports = {
  "publicPath": "/",
  "assetsDir": "static",
  "devServer": {
    "proxy": {
      "^/api": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/admin": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/media": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/static": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
    }
  },
  productionSourceMap: false,

}
