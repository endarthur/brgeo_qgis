# QML do Mapa Geológico do Brasil ao Milionésimo
Um arquivo de estilo (.qml) para o mapa geológico do Brasil ao milionésimo (http://www.cprm.gov.br/publique/Geologia/Apresentacao-202). Foi produzido a partir da correção
manual do arquivo de definição para o ArcGIS (disponível em http://geosgb.cprm.gov.br/geosgb/media/bibliotecas_fontes_arcgis.zip),
conversão para o formato SLD utilizando a ferramenta ArcGIS-Map to SLD converter (disponível em http://arcmap2sld.i3mainz.hs-mainz.de/ArcMap2SLDConverter_Eng.htm) e finalmente transcrevendo as informações de cor do SLD resultante para um arquivo QML utilizando o script sld_to_qml.py incluso neste repositório.

# Brazil to the Millionth Geological Map QML
A QGIS qml layer styling file for lithology layers for the Brazil to the Millionth scale geological map (http://www.cprm.gov.br/en/Geology/The-Geological-Map-of-Brazil---Scale-1%3A1.000.000-4174.html). It was made by first manually fixing missing the original ArcGIS layer definition files (available at http://geosgb.cprm.gov.br/geosgb/media/bibliotecas_fontes_arcgis.zip), conversion to the SLD format using to ArcGIS-Map to SLD converter tool (avaiable at http://arcmap2sld.i3mainz.hs-mainz.de/ArcMap2SLDConverter_Eng.htm) and finally transcribing the SLD color data to a QML file using the sld_to_qml.py script included in this repository.

## Thanks
We would like to thank Albrecht Weiser, author of the ArcGIS-Map to SLD converter. We would also like to thank professor Ginaldo Ademar da Cruz Campanha (IGc-USP, São Paulo) for feedback on missing units from previous versions of the QML file.
