import axios from "axios";

const instance = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? 'https://wstanley.ru' : 'http://127.0.0.1:8000',
  // timeout: 199000,
});

export default instance;