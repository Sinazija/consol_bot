# consol_bot
Це консольноий бот помічник, який розпізнаэ команди, що вводяться з клавіатури, і відповідає відповідно до введеної команди.
Функції бота:
* Бот перебуває в безкінечному циклі, чекаючи команди користувача.
* Бот завершує свою роботу, якщо зустрічає слова: .
* Бот не чутливий до регістру введених команд.
* Бот приймає команди:
- "hello", відповідає у консоль "How can I help you?"
- "add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
- "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
- "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... користувач вводить ім'я контакту, чий номер треба показати.
- "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
- "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".