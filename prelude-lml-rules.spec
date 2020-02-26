Summary:	Ruleset for Prelude LML pcre plugin
Summary(pl.UTF-8):	Zestaw reguł dla wtyczki pcre Prelude LML
Name:		prelude-lml-rules
Version:	5.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Networking
#Source0Download: https://www.prelude-siem.org/projects/prelude/files
Source0:	https://www.prelude-siem.org/attachments/download/1174/%{name}-%{version}.tar.gz
# Source0-md5:	3c686aafd05630e2f51eef5a3313a981
URL:		https://www.prelude-siem.org/
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
Requires:	prelude-lml >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruleset for Prelude LML pcre plugin (<https://www.prelude-siem.org/>).
These rules are brought to you by CS and the Prelude Community.

%description -l pl.UTF-8
Zestaw reguł dla wtyczki pcre systemu Prelude LML
(<https://www.prelude-siem.org/>). Zostały udostępnione przez CS oraz
Społeczność Prelude.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' src/prelude-lml-rules-check

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/prelude-lml,%{_bindir}}

cp -r ruleset $RPM_BUILD_ROOT%{_sysconfdir}/prelude-lml
cp -p src/prelude-lml-rules-check $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/prelude-lml-rules-check
%{_sysconfdir}/prelude-lml/ruleset
