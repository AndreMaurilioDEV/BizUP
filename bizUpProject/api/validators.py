def validate_data(self, data):
      errors = []

      if 'nome' not in data or not data['nome'].isalpha:
          errors.append({"field": "nome", "error": "O nome deve apenas conter letras"})

      if 'nome' not in data or len(data['nome']) < 3:
          errors.append({"field": "nome", "error": "O nome deve ter pelo menos 3 caracteres."})

      if 'email' not in data or not data['email'].endswith('@example.com'):
          errors.append({"field": "email", "error": "O email deve ser do domínio '@example.com'."})

      if 'cpf' not in data or len(data['cpf']) != 11:
          errors.append({"field": "cpf", "error": "O CPF deve ter 11 dígitos."})

      return errors