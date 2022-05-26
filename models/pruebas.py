from werkzeug.security import check_password_hash,generate_password_hash
print(generate_password_hash('root'))
print(check_password_hash('pbkdf2:sha256:260000$BfFilGtLYmwcsySQ$686ee0837a03ddbd1fba4780d8b6edb97740057f15d190d39b2cd6cf572f5a61','root'))