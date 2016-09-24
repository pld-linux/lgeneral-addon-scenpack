Summary:	LGeneral game - collection of Panzer General scenarios from various authors
Summary(pl.UTF-8):	Gra Linux General - zbiór scenariuszy różnych autorów dla gry Panzer General
Name:		lgeneral-addon-scenpack
Version:	20110815
Release:	1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/scenpack.zip
# Source0-md5:	f6a2e646571c87f6985a8c087d3fcc91
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
Requires:	lgeneral-data-pg
# contains all scenarios present in old lgeneral-contrib-0.1 package
Obsoletes:	lgeneral-contrib < 0.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Scenario Pack - a collection of Panzer
General scenarios from various authors.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera Scenario Pack - zbiór scenariuszy różnych autorów
dla gry Panzer General.

%prep
%setup -q -n scenpack

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a gfx nations scenarios $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt readme.txt info
%{_datadir}/lgeneral/gfx/flags/Iceland1942.bmp
%{_datadir}/lgeneral/gfx/flags/pacific.bmp
%{_datadir}/lgeneral/gfx/units/Berlin1946.bmp
%{_datadir}/lgeneral/gfx/units/Demjansk.bmp
%{_datadir}/lgeneral/gfx/units/Gazala.bmp
%{_datadir}/lgeneral/gfx/units/Gothic.bmp
%{_datadir}/lgeneral/nations/Iceland1942.ndb
%{_datadir}/lgeneral/nations/pacific.ndb
%{_datadir}/lgeneral/scenarios/Aachen
%{_datadir}/lgeneral/scenarios/Arhnem
%{_datadir}/lgeneral/scenarios/Austria
%{_datadir}/lgeneral/scenarios/Avalanche
%{_datadir}/lgeneral/scenarios/Azores
%{_datadir}/lgeneral/scenarios/Baku
%{_datadir}/lgeneral/scenarios/Balka1944
%{_datadir}/lgeneral/scenarios/Barbarossa1942
%{_datadir}/lgeneral/scenarios/Bastogne
%{_datadir}/lgeneral/scenarios/Berlin1946
%{_datadir}/lgeneral/scenarios/Bismarck
%{_datadir}/lgeneral/scenarios/Carentan
%{_datadir}/lgeneral/scenarios/Casino
%{_datadir}/lgeneral/scenarios/CityFight
%{_datadir}/lgeneral/scenarios/Demjansk
%{_datadir}/lgeneral/scenarios/Denmark
%{_datadir}/lgeneral/scenarios/DoggerBank
%{_datadir}/lgeneral/scenarios/Dunkirk
%{_datadir}/lgeneral/scenarios/Dyle
%{_datadir}/lgeneral/scenarios/Falaise
%{_datadir}/lgeneral/scenarios/Falk82
%{_datadir}/lgeneral/scenarios/France1944
%{_datadir}/lgeneral/scenarios/Gazala
%{_datadir}/lgeneral/scenarios/Gibraltar
%{_datadir}/lgeneral/scenarios/Gothic
%{_datadir}/lgeneral/scenarios/GreekIslands
%{_datadir}/lgeneral/scenarios/Holland
%{_datadir}/lgeneral/scenarios/Iceland1942
%{_datadir}/lgeneral/scenarios/Italy1943
%{_datadir}/lgeneral/scenarios/Korea
%{_datadir}/lgeneral/scenarios/Kurland
%{_datadir}/lgeneral/scenarios/Malta
%{_datadir}/lgeneral/scenarios/Midway
%{_datadir}/lgeneral/scenarios/Motti
%{_datadir}/lgeneral/scenarios/Norway45
%{_datadir}/lgeneral/scenarios/Papagos_plus
%{_datadir}/lgeneral/scenarios/Poland45
%{_datadir}/lgeneral/scenarios/ThreeBridges
%{_datadir}/lgeneral/scenarios/WakeIsland
%{_datadir}/lgeneral/scenarios/Westerplatte
