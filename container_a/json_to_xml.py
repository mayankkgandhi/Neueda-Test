def json_to_xml_coverter(data):
    """
    Function to convert Json to XML
    :param: data - json data for xml converstion
    :return: xml - converted xml data
    """
    xml = "<root>"
    for key,value in data.items():
        xml += "<" + key + ">"
        xml = json_value_converter(xml, value)
        xml += "</" + key + ">"
    xml += "</root>"
    return xml


def json_value_converter(xml, value):
    """
    Recursive function to convert json values for xml
    :param: xml - xml data
    :param: value - json value
    :return: xml - converted xml data
    """
    if isinstance(value, int) or isinstance(value, float):
        xml += str(value)
    else:
        if isinstance(value, str):
            xml += value
        elif isinstance(value, list) or isinstance(value, tuple):
            for each in value:
                xml += '<item>'
                xml = json_value_converter(xml, each)
                xml += '</item>'
        elif isinstance(value, dict):
            for value_key, value_value in value.items():
                xml += '<' + value_key + '>'
                xml = json_value_converter(xml, value_value)
                xml += '</' + value_key + '>'
    return xml
