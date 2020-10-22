def test_calculo_salario_base():
    # Arrange
    qde_dependentes = 5
    salario = 3000
    expectativa = salario - (salario * 0.11) - (189.59 * qde_dependentes)


    # Act
    from domain.logic import calculo_salario_base
    resultado = calculo_salario_base(salario, qde_dependentes)


    # Assert
    assert resultado == expectativa
