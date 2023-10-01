from openpyxl import Workbook


def make_excel_report(robots_list: list[tuple[str, str, int]]) -> Workbook:
    sheets = {robot[0] for robot in robots_list}
    wb = Workbook()
    for num, name in enumerate(sheets):
        wb.create_sheet(name, num).append(
            ['Модель', 'Версия', 'Количество за неделю']
        )
    for robot in robots_list:
        wb[robot[0]].append(robot)
    return wb
