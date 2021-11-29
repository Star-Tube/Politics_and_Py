""" Imports Go Here """
import requests

import logging

log = logging.getLogger(__name__)

# Set Global Variables
_Key = ""


def key(value):
    global _Key
    _Key = value


# Set Class Nations()
class Nations(list):
    nations_url = f"http://politicsandwar.com/api/nations/?key={_Key}"

    def __init__(self):
        super().__init__()

    def base(self):
        nations_dict = requests.get(self.nations_url).text
        for nid in self:
            next(nation for nation in nations_dict if nation["id"] == nid)


# Set Class Nation()
class Nation:
    """
    Nation(nid=152003)

    Use to store lots of nation data. Store many nations in Nations().
    """
    __slots__ = "nid", "name", "aa", "aaid", "aapos", "leader", "continent", "war_policy", "color", "cities", "infra",\
                "off_war", "def_war", "score", "rank", "vm", "minutes_inactive", "api_response", "nation_api"

    def __init__(self, nid=None, aa=None, name=None, leader=None, aaid=None, aapos=None, continent=None,
                 war_policy=None, color=None, cities=None, infra=None, off_war=None, def_war=None, score=None,
                 rank=None, vm=None, minutes_inactive=None, call=False):
        self.update(nid=nid, aa=aa, name=name, leader=leader, aaid=aaid, aapos=aapos, continent=continent,
                    war_policy=war_policy, color=color, cities=cities, infra=infra, off_war=off_war, def_war=def_war,
                    score=score, rank=rank, vm=vm, minutes_inactive=minutes_inactive, call=call)

    def update(self, nid=None, aa=None, name=None, leader=None, aaid=None, aapos=None, continent=None, war_policy=None,
               color=None, cities=None, infra=None, off_war=None, def_war=None, score=None, rank=None, vm=None,
               minutes_inactive=None, call=False):
        log.debug(f"Updating {nid}'s base stats")
        if nid is not None:
            self.nid = nid
        if self.nid is int or str and call:
            self.nation_api = f"http://politicsandwar.com/api/nation/id={self.nid}/&key={_Key}"
            log.debug(f"Calling {self.nation_api}")
            api_response = requests.get(self.nation_api).json()
            log.debug("Call complete")
            self.aa = api_response["alliance"]
            self.aaid = api_response["allianceid"]
            self.aapos = api_response["allianceposition"]
            self.name = api_response["name"]
            self.leader = api_response["leadername"]
            self.continent = api_response["continent"]
            self.war_policy = api_response["war_policy"]
            self.color = api_response["color"]
            self.cities = api_response["cities"]
            self.infra = api_response["totalinfrastructure"]
            self.off_war = api_response["offensivewars"]
            self.def_war = api_response["defensivewars"]
            self.score = api_response["score"]
            self.rank = api_response["nationrank"]
            self.vm = api_response["vmode"]
            self.minutes_inactive = api_response["minutessinceactive"]
        if aa is not None:
            self.aa = aa
        if aaid is not None:
            self.aaid = aaid
        if aapos is not None:
            self.aapos = aapos
        if name is not None:
            self.name = name
        if leader is not None:
            self.leader = leader
        if continent is not None:
            self.continent = continent
        if war_policy is not None:
            self.war_policy = war_policy
        if color is not None:
            self.color = color
        if cities is not None:
            self.cities = cities
        if infra is not None:
            self.infra = infra
        if off_war is not None:
            self.off_war = off_war
        if def_war is not None:
            self.def_war = def_war
        if score is not None:
            self.score = score
        if rank is not None:
            self.rank = rank
        if vm is not None:
            self.vm = vm
        if minutes_inactive is not None:
            self.minutes_inactive = minutes_inactive

    def values(self):
        for x in self.__slots__:
            try:
                yield x, self.__getattribute__(x)
            except AttributeError:
                logging.debug(f"No Value for {x}")


class City:
    __slots__ = 'cityid', 'name', 'nationid', 'nation', 'leader', 'continent', 'founded', 'age', 'powered', \
                'infra', 'land', 'population', 'crime', 'disease', 'pollution', 'commerce', 'powered', 'coal_pp', 'oil_pp', 'nuclear_pp', 'wind_pp', 'coal_mine', 'oil_well', \
                'lead_mine', 'uranium_mine', 'iron_mine', 'bauxite_mine', 'farms', 'gas', 'steel', 'aluminum', \
                'munitions', 'police_stations', 'hospitals', 'recycling_centers', 'subways', 'supermarkets', \
                'banks', 'shopping_malls', 'stadiums', 'barracks', 'factories', 'hangers', 'drydocks', 'infra_used', \
                'improvements'

    def __init__(self, cityid=None, name=None, nationid=None, nation=None, founded=None, age=None, powered=None,
                 infra=None, land=None, call=False):
        self.update(cityid=cityid, name=name, nationid=nationid, nation=nation, founded=founded, age=age,
                    powered=powered, infra=infra, land=land, call=call)

    def __str__(self):
        return f"The city of {self.name}"

    def update(self, cityid=None, name=None, nationid=None, nation=None, founded=None, age=None, powered=None,
               infra=None, land=None, call=False):
        if cityid is not None:
            self.cityid = cityid
        if self.cityid is not None and call:
            log.debug(f"Calling https://politicsandwar.com/api/city/id={self.cityid}&key={_Key}")
            api_response = requests.get(f"https://politicsandwar.com/api/city/id={self.cityid}&key={_Key}").json()
            self.name = api_response["name"]
            self.nationid = api_response["nationid"]
            self.nation = api_response["nation"]
            self.founded = api_response["founded"]
            self.age = api_response["age"]
            self.powered = api_response["powered"]
            self.infra = api_response["infrastructure"]
            self.land = api_response["land"]
        if name is not None:
            self.name = name
        if nationid is not None:
            self.nationid = nationid
        if nation is not None:
            self.nation = nation
        if founded is not None:
            self.founded = founded
        if age is not None:
            self.age = age
        if powered is not None:
            self.powered = powered
        if infra is not None:
            self.infra = infra
        if land is not None:
            self.land = land

    def build_update(self):
        api_response = requests.get(f"https://politicsandwar.com/api/city_export.php?city_id={self.cityid}").json()
        self.infra_used = api_response["infra_needed"]
        self.improvements = api_response["imp_total"]
        self.coal_pp = api_response["imp_coalpower"]
        self.oil_pp = api_response["imp_oilpower"]
        self.wind_pp = api_response["imp_windpower"]
        self.nuclear_pp = api_response["imp_nuclearpower"]
        self.coal_mine = api_response["imp_coalmine"]
        self.oil_well = api_response["imp_oilwell"]
        self.uranium_mine = api_response["imp_uramine"]
        self.lead_mine = api_response["imp_leadmine"]
        self.iron_mine = api_response["imp_ironmine"]
        self.bauxite_mine = api_response["imp_bauxitemine"]
        self.farms = api_response["imp_farm"]
        self.gas = api_response["imp_gasrefinery"]
        self.aluminum = api_response["imp_aluminumrefinery"]
        self.munitions = api_response["imp_munitionsfactory"]
        self.steel = api_response["imp_steelmill"]
        self.police_stations = api_response["imp_policestation"]
        self.hospitals = api_response["imp_hospital"]
        self.recycling_centers = api_response["imp_recyclingcenter"]
        self.subways = api_response["imp_subway"]
        self.supermarkets = api_response["imp_supermarket"]
        self.banks = api_response["imp_bank"]
        self.shopping_malls = api_response["imp_mall"]
        self.stadiums = api_response["imp_stadium"]
        self.barracks = api_response["imp_barracks"]
        self.factories = api_response["imp_factory"]
        self.hangers = api_response["imp_hangars"]
        self.drydocks = api_response["imp_drydock"]
        return api_response

    def popdensity(self) -> int:
        return self.population/self.land

    def values(self) -> tuple:
        for x in self.__slots__:
            try:
                yield x, self.__getattribute__(x)
            except AttributeError:
                logging.log(level=0, msg=f"None value found for {x}")
                yield x, None

    def city_mil(self) -> dict:
        mil = {
            "barracks": self.barracks,
            "factories": self.factories,
            "hangers": self.hangers,
            "drydocks": self.drydocks
        }
        return mil


def main():
    """
    main()
    Code Goes Here
    """
    print("This is a package. Import me into your program and use me to make your wettest dreams come true.")
    global _Key
    mel = City(276893)
    mel.update(call=True)
    mel.build_update()
    for value in mel.values():
        print(value)


if __name__ == '__main__':
    """
    If run directly then do main()
    """
    logging.basicConfig(level=0)
    main()
