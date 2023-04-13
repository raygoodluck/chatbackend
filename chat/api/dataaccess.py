from chat.models import SiteSetting
from chat.models import DictItem


def getSetting(name):
    settingItems = SiteSetting.objects.filter(
        name=name,
    )
    if len(settingItems) > 0:
        openai_api_key = settingItems[0].value
        return openai_api_key
    raise Exception(f"Not found {name}")


def getDictItems(name: str):
    dictItems = DictItem.objects.filter(parent__name=name, parent__is_hidden=False)
    dict = {}
    for item in dictItems:
        dict[item.name] = item.value
    return dict
