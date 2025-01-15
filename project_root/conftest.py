import pytest

def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    Добавляет сводную информацию в вывод консоли после выполнения тестов.
    """
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    warnings = len(terminalreporter.stats.get("warnings", []))

    total = passed + failed + skipped

    terminalreporter.section("Тестовая статистика")
    terminalreporter.write_line(f"Общее количество тестов: {total}")
    terminalreporter.write_line(f"Пройдено: {passed}")
    terminalreporter.write_line(f"Провалено: {failed}")
    terminalreporter.write_line(f"Пропущено: {skipped}")
    terminalreporter.write_line(f"Предупреждений: {warnings}")

    if failed > 0:
        terminalreporter.write_line("\nОбщие замечания:")
        terminalreporter.write_line(" - Проверьте логи для анализа причин ошибок.")
        terminalreporter.write_line(" - Убедитесь, что тесты соответствуют ожидаемым данным.")
    else:
        terminalreporter.write_line("\nВсе тесты успешно пройдены!")

