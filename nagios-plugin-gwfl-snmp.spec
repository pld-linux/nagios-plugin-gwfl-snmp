# TODO
# - default check_command in .cfg file
%define		_proj_name	gwfl-nagios-plugins
Summary:	GWFL snmp checks for nagios
Name:		nagios-plugin-gwfl-snmp
Version:	2.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://gwfl.daimonic.org/files/%{_proj_name}-%{version}.tar.gz
# Source0-md5:	14d3fa6075107d7a2decb02724d506e2
Patch0:		%{_proj_name}.v2.patch
URL:		http://gwfl.daimonic.org/index.pl?p=nagiosplugs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GWFL snmp checks for nagios check_snmp_mem_free check_snmp_mem_used
check_snmp_cpu check_snmp_disk check_snmp_fans check_snmp_load
check_snmp_phydrv check_snmp_psus check_snmp_swap check_snmp_temps
check_snmp_totalprocs

%prep
%setup -q -n %{_proj_name}-%{version}
%patch0 -p 1

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
