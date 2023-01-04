# arxml-simple-view

```
python arxml-simple-view.py sample.arxml
```

Input `sample.arxml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00047.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>ara</SHORT-NAME>
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>diag</SHORT-NAME>
          <AR-PACKAGES>
            <AR-PACKAGE>
              <SHORT-NAME>example</SHORT-NAME>
              <ELEMENTS>
                <SERVICE-INTERFACE>
                  <SHORT-NAME>AddInterface</SHORT-NAME>
                  <NAMESPACES>
                    <SYMBOL-PROPS>
                      <SHORT-NAME>ara</SHORT-NAME>
                      <SYMBOL>ara</SYMBOL>
                    </SYMBOL-PROPS>
                    <SYMBOL-PROPS>
                      <SHORT-NAME>diag</SHORT-NAME>
                      <SYMBOL>diag</SYMBOL>
                    </SYMBOL-PROPS>
                    <SYMBOL-PROPS>
                      <SHORT-NAME>example</SHORT-NAME>
                      <SYMBOL>example</SYMBOL>
                    </SYMBOL-PROPS>
                  </NAMESPACES>
                ...
```

Output `sample.arxml.simple.txt`

```xml
<AUTOSAR>
	<AR-PACKAGES>
		<AR-PACKAGE> [ara]
			<SHORT-NAME>
			<AR-PACKAGES>
				<AR-PACKAGE> [diag]
					<SHORT-NAME>
					<AR-PACKAGES>
						<AR-PACKAGE> [example]
							<SHORT-NAME>
							<ELEMENTS>
								<SERVICE-INTERFACE> [AddInterface]
									<SHORT-NAME>
									<NAMESPACES>
										<SYMBOL-PROPS> [ara]
											<SHORT-NAME>
											<SYMBOL>
										<SYMBOL-PROPS> [diag]
											<SHORT-NAME>
											<SYMBOL>
										<SYMBOL-PROPS> [example]
											<SHORT-NAME>
											<SYMBOL>
```