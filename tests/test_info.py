import pytest
from govsic.data.sections import description
from govsic.exceptions import InvalidSICCodeError
from govsic.sic import SIC


def test_summary_valid():
    with pytest.raises(InvalidSICCodeError) as exc_info:
        sic = SIC(12345)
        print(sic.summary())

    exception_raised = exc_info.value
    assert str(exception_raised) == (
        "The code provided is not in the official SIC glossary."
    )

SUMMARY_TEST_EXAMPLES = [
    (
        SIC("46000"),
        description("""
            [G] 46.00/0 :: WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES
            2-digit description:
            This section includes wholesale and retail sale (i.e. sale without transformation) of any type of goods, and the supply of services incidental to the sale of merchandise. Wholesaling and retailing are the final steps in the distribution of merchandise. Also included in this section are the repair of motor vehicles and motorcycles.
            Sale without transformation is considered to include the usual operations (or manipulations) associated with trade, for example sorting, grading and assembling of goods, mixing (blending) of goods (for example sand), bottling (with or without preceding bottle cleaning), packing, breaking bulk and repacking for distribution in smaller lots, storage (whether or not frozen or chilled).
            Division 45 includes all activities related to the sale and repair of motor vehicles and motorcycles, while divisions 46 and 47 include all other sale activities. The distinction between division 46 (wholesale) and division 47 (retail sale) is based on the predominant type of customer.
            Wholesale is the resale (sale without transformation) of new and used goods to retailers, business to business trade such as to industrial, commercial, institutional or professional users, or resale to other wholesalers, or involves acting as an agent or broker in buying merchandise for, or selling merchandise to, such persons or companies. The principal types of businesses included are merchant wholesalers, i.e. wholesalers who take title to the goods they sell, such as wholesale merchants or jobbers, industrial distributors, exporters, importers, and cooperative buying associations, sales branches and sales offices (but not retail stores) that are maintained by manufacturing or mining units apart from their plants or mines for the purpose of marketing their products and that do not merely take orders to be filled by direct shipments from the plants or mines. Also included are merchandise and commodity brokers, commission merchants and agents and assemblers, buyers and cooperative associations engaged in the marketing of farm products.
            Wholesalers frequently physically assemble, sort and grade goods in large lots, break bulk, repack and redistribute in smaller lots, for example pharmaceuticals; store, refrigerate, deliver and install goods, engage in sales promotion for their customers and label design.
            Retailing is the resale (sale without transformation) of new and used goods mainly to the general public for personal or household consumption or utilisation, by shops, department stores, stalls, mail-order houses, door-to-door sales persons, hawkers, consumer cooperatives, auction houses etc. Most retailers take title to the goods they sell, but some act as agents for a principal and sell either on consignment or on a commission basis.
        """)
    ),
    (
        SIC("46300"),
        description("""
            [G] 46.30/0 :: WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES
            3-digit description:
            Wholesale of food, beverages and tobacco
        """)
    ),
    (
        SIC("46342"),
        description("""
            [G] 46.34/2 :: WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES
            5-digit description:
            Wholesale of wine, beer, spirits and other alcoholic beverages
        """)
    )
]

@pytest.mark.parametrize(
    "sic, expectation",
    SUMMARY_TEST_EXAMPLES
)
def test_summary_print(sic: SIC, expectation: str):
    summary = sic.summary()
    assert summary == expectation
