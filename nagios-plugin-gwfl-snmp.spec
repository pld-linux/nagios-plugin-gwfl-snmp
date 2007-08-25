# TODO
# - optflags
# - default check_command in .cfg file
%define		proj_name	gwfl-nagios-plugins
Summary:	GWFL SNMP checks for Nagios
Summary(pl.UTF-8):	Testy GWFL SNMP dla Nagiosa
Name:		nagios-plugin-gwfl-snmp
Version:	2.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://gwfl.daimonic.org/files/%{proj_name}-%{version}.tar.gz
# Source0-md5:	14d3fa6075107d7a2decb02724d506e2
Patch0:		%{proj_name}.v2.patch
URL:		http://gwfl.daimonic.org/index.pl?p=nagiosplugs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nagios plugins to check HP ProLiant systems, Netscreen firewalls,
Cisco switches, Cisco Content Switches, RFC 1628 UPS systems, eSensors
HVAC EM01 environmental monitor, and router interfaces over SNMP.

%description -l pl.UTF-8
Wtyczki Nagiosa do sprawdzania po SNMP systemów HP ProLiant, firewalli
Netscreen, switchy Cisco, switchy Cisco Content, systemów UPS zgodnych
z RFC 1628, monitorów środowiskowych HVAC EM01 oraz interfejsów
routerów.

%prep
%setup -q -n %{proj_name}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nagios/plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_libdir}/nagios/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/nagios/plugins/*
