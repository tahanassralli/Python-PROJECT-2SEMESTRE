jQuery(function ($) {
        function createFirstGridData(count) {
            var data = [];
            for (var i = 0; i < count; i++) {
                data.push({
                    id: i,
                    year: 2000 + i,
                    price: 1000 - i
                });
            }
            return data;
        }

        function createSecondGridData(count) {
            var data = [];
            for (var i = 0; i < count; i++) {
                for (var j = 0; j < count; j++) {
                    data.push({
                        id: j + i,
                        productsCount: (j + i + i),
                        parentID: i
                    });
                }
            }
            return data;
        }

        $("#grid1").shieldGrid({
            dataSource: {
                data: createFirstGridData(10)
            },
            paging: {
                pageSize: 5
            },
            selection: {
                type: "row",
                multiple: false
            },
            events: {
                selectionChanged: function (e) {
                    $("#hint").hide();

                    var selectedItemID = $("#grid1").swidget().contentTable.find(".sui-selected").get(0).cells[0].innerHTML;
                    var secondGrid = $("#grid2").swidget();
                    if (secondGrid) {
                        secondGrid.dataSource.filter.value = selectedItemID;
                        secondGrid.refresh();
                    }
                    else {
                        $("#grid2").shieldGrid({
                            dataSource: {
                                data: createSecondGridData(10),
                                filter: { path: "id", filter: "eq", value: selectedItemID }
                            },
                            paging: true,
                            columns: [
                                { field: "id", width: "100px", title: "ID" },
                                { field: "productsCount", title: "Products Count" },
                                { field: "parentID", title: "Parent ID" }
                            ]
                        });
                    }
                }
            },
            columns: [
                { field: "id", width: "70px", title: "ID" },
                { field: "year", title: "Year" },
                { field: "price", title: "Price" }
            ]
        });
    });
