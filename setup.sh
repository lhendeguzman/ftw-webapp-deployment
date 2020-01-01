mkdir -p ~/streamlit/

echo "\
[generate]\n\
email = \"contactlhen@gmail.com\" "\n\
" > ~/.stramlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config/toml