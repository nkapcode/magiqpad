const config = {
    apiHostname: process.env.REACT_APP_API_HOSTNAME || 'localhost:8000',
    apiBaseUrl: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1',
    authBaseUrl: process.env.REACT_APP_AUTH_BASE_URL || 'http://localhost:8000/auth',
};

module.exports = config;
