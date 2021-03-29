# Strategy

Esse padrão é utilizado para alterar comportamentos de classes sem estendê-la.

Podemos percebe-lo quando um método de uma classe delega um algoritmo para outra classe,
como no nosso exemplo, o due() do Order, que delega o cálculo de promoções à outras classes.
Assim, se quisermos adicionar novas promoções, não mexeremos na classe Order.
